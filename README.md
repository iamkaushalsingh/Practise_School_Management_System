# School Management System Project 

## Installation and Running Instructions :
- A seperate wiki [INSTALL.md](INSTALL.md) is written for this purpose.

## Overview:
The School Management System is a web application designed to facilitate the management of internships and applications for students and teachers. It provides a platform where teachers can post internship opportunities and students can view and apply for these internships.

## Features:
### User Roles:
#### Student:
- Can sign up with email and password.
- Can view a dashboard showing a list of available internships.
- Can apply for internships.
- Can view applied internships in their profile.
- Profile contains information like name, registration number, address, email, phone, department, and batch.

#### Teacher:
- Can sign up with email and password.
- Can view a dashboard listing students who have applied for their posted internships.
- Can post new internship opportunities.
- Can edit and delete their posted internships.
- Profile contains basic information.

### Authentication:
- Students and teachers can sign up and log in to their respective accounts.
- Authentication is done using email and password.

### Internship Management:
- Teachers can post new internship opportunities.
- Students can view a list of available internships on their dashboard.
- Students can apply for internships.
- Teachers can view a list of students who have applied for their internships.

### Profile Management:
- Students and teachers can update their profiles.
- #### Profile information includes:
  - Student: Name, registration number, address, email, phone, department, and batch.
  - Teacher: Name, teacher id, email, phone, address, department

## Dashboard:
### Student Dashboard:
- Shows a list of available internships.
- Provides a button/link to apply for each internship.

### Teacher Dashboard:
- Lists students who have applied for each posted internship.

## User Flow:
### Student Workflow:
1. Student logs in or signs up.
2. After logging in, the student lands on the dashboard.
3. Dashboard shows a list of available internships.
4. Student can view internship details and apply.
5. Applied internships are listed in the profile.
   
### Teacher Workflow:
1. Teacher logs in or signs up.
2. After logging in, the teacher lands on the dashboard.
3. Dashboard shows a list of posted internships.
4. Teacher can add/edit/delete internships.
5. Teacher can view a list of students who have applied for each internship.

## Additional Details:
- The project uses Django as the backend framework.
- It implements Django's authentication system for user management.
- Each internship posting includes details like internship title, description, salary, etc.
- Teachers can add/edit/delete internship postings.
- Students can view internship postings and apply.
- Profile information is displayed in a structured format for both students and teachers.
- One student can apply for only one internship. It can also be a research Internship
