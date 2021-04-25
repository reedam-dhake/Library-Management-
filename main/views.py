from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
import re, datetime, schedule, time, pytz
from django.contrib.auth.forms import UserChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

class HomeView(ListView):
	model = BookName
	template_name = 'home.html'

def book_detail(request, pk):
	for borrower in Borrower.objects.all():
		stid = borrower.student.id
		bid = borrower.book.id
		student1 = Student.objects.get(id=stid)
		book1 = BookName.objects.get(id=bid)
		print(borrower.return_date <= timezone.now())
		if borrower.return_date <= timezone.now():
			subject = 'Due date of ' + book1.name + ' has passed.'
			message = 'As the due date has passed already your access to view the pdf is revoked.'
			email_from = settings.EMAIL_HOST_USER
			recipient = [student1.user.email,]
			send_mail( subject, message, email_from, recipient )
			borrower.delete()
			try:
				borrower2 = Borrower.objects.filter(book=book1,waiting_list=True).order_by('issue_date')[0]
				borrower2.waiting_list = False
				borrower2.issue_date = timezone.now()
				borrower2.return_date = borrower2.issue_date + timezone.timedelta(days=7)
				borrower2.save()
				subject = book1.name + ' issued to you.'
				message = 'You have been issued this book for 7 days.'
				email_from = settings.EMAIL_HOST_USER
				recipient = [borrower2.student.user.email,]
				send_mail( subject, message, email_from, recipient )
			except ObjectDoesNotExist:
				student1.total_books_due = F('total_books_due') - 1
				student1.save()
				book1.available_copies = F('available_copies') + 1
				book1.save()

	template_name = 'detail.html'
	book = get_object_or_404(BookName, pk=pk)
	comments = book.comments.filter(active=True)
	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=True)
			new_comment.post = book
			new_comment.user = request.user
			new_comment.save()
	else:
		comment_form = CommentForm()
	try:
		obj = Borrower.objects.get(book=BookName.objects.get(id=pk),student=Student.objects.get(user=request.user))
	except (ObjectDoesNotExist ,TypeError):
		return render(request, template_name, {'object': book,
											   'comments': comments,
											   'new_comment': new_comment,
											   'comment_form': comment_form})
	
	return render(request, template_name, {'object': book,
										   'comments': comments,
										   'new_comment': new_comment,
										   'comment_form': comment_form,
										   'borrow': obj})

def comment_Delete(request,pk):
	comment_1 = get_object_or_404(Comment, pk=pk)
	if request.method == 'POST':
		subject = 'Inappropriate Comment'
		message = 'This is a warning to you for posting an inaapropriate comment.'
		email_from = settings.EMAIL_HOST_USER
		recipient = [comment_1.user.email,]
		send_mail( subject, message, email_from, recipient )
		comment_1.active = False
		comment_1.save()
		return redirect('home')
	return render(request,'deleteComment.html',locals() )


class AddBookView(CreateView):
	model = BookName
	form_class = AddNewBook
	template_name = 'addBook.html'

class EditDetailView(UpdateView):
	model = BookName
	form_class = AddNewBook
	template_name = 'editDetail.html'

class DeleteBookView(DeleteView):
	model = BookName
	template_name = 'deleteBook.html'
	success_url = reverse_lazy('home')

def bookListView(request):
	book_list = BookName.objects.all()
	return render(request, 'home.html', locals())

def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
	query = None 
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query



def search_book(request):
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']

		entry_query = get_query(query_string, ['name','author'])

		book_list= BookName.objects.filter(entry_query)

	return render(request,'home.html',locals() )

def student_request_issue(request, pk):
	current_user = request.user
	obj = BookName.objects.get(id=pk)
	stu=Student.objects.get(user=current_user)
	s = get_object_or_404(Student, user=current_user)
	if stu.total_books_due < 10:
		if obj.available_copies > 0:
			message = "Book has been issued, You can view the Pdf now."
			a = Borrower()
			a.student = s
			a.book = obj
			a.issue_date = timezone.now()
			a.return_date = a.issue_date + timezone.timedelta(days=7)
			obj.available_copies = obj.available_copies - 1
			obj.save()
			stu.total_books_due=stu.total_books_due+1
			stu.save()
			a.save()
		else:
			message = "Added to Waitlist"
			a = Borrower()
			a.student = s
			a.book = obj
			a.issue_date = timezone.now()
			a.return_date = a.issue_date + timezone.timedelta(days=100)
			obj.save()
			a.waiting_list = True
			a.save()
	else:
		message = "you have exceeded limit."
	return render(request, 'issue.html', locals())

def return_book(request, pk):
	obj = Borrower.objects.get(book=BookName.objects.get(id=pk),student=Student.objects.get(user=request.user))
	student_pk=obj.student.id
	student = Student.objects.get(id=student_pk)
	student.total_books_due=student.total_books_due-1
	student.save()
	book=BookName.objects.get(id=pk)
	book.available_copies=book.available_copies+1
	book.save()
	obj.delete()
	return redirect('home')

def StudentList(request):
	students = Student.objects.all()
	return render(request, 'student_list.html', locals())

def StudentDetail(request, pk):
	student = get_object_or_404(Student, id=pk)
	books=Borrower.objects.filter(student=student)
	return render(request, 'student_detail.html', locals())

def search_student(request):
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']

		entry_query = get_query(query_string, ['name'])

		students= Student.objects.filter(entry_query)

	return render(request,'student_list.html',locals())


def make_staff(request,pk):
	student = get_object_or_404(Student, pk=pk)
	user = student.user
	user.is_staff = True
	user.save()
	return redirect('student_list')

def unmake_staff(request,pk):
	student = get_object_or_404(Student, pk=pk)
	user = student.user
	user.is_staff = False
	user.save()
	return redirect('student_list')

def extend_date(request,pk):
	obj = Borrower.objects.get(book=BookName.objects.get(id=pk),student=Student.objects.get(user=request.user))
	obj.return_date = obj.return_date + timezone.timedelta(days=1)
	obj.save()
	return redirect('home')