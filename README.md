# Maxxi Tani Task API CRUD
<p align="center"><a href="" target="_blank"><img src="https://images.glints.com/unsafe/glints-dashboard.s3.amazonaws.com/company-logo/fc738e23ad0fa6b614955a8b21aa02e9.png" width="400"></a></p>

##  Requirement Endpoint
1. **[POST] /employees/** to add employee data
2. **[PUT] /employees/** to change employee data
3. **[DELETE] /employees/** to delete employee data
4. **[GET] /employees** to display data on all employee data, sorted
alphabetically
5. **[GET] /employees/<employee-number-id>** displays the details of 1 particular employee
6. **[GET] /employee/divisions/<id-division>** displays a list of employees from a particular division

#  How to Setup a Project You Cloned from Github.com

Requirement:
```markdown
Python 3.11.4
```
1. Clone GitHub repo for this project locally
```markdown

git clone https://github.com/alfinyusriansyah/maxxi-tani-task-API-CRUD

```
2. After Clone Github repo. Create file .env to connect database, adjust the contents according to the needs of the database  : 
```markdown
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
```

3. Running 
```markdown

python app.py

```
