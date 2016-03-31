##Markdown References
* [Mastering Markdown] (https://guides.github.com/features/mastering-markdown/#syntax)
* Writing on GitHub/[Basic writing and formatting syntax] (https://help.github.com/articles/basic-writing-and-formatting-syntax/)
* Writing on GitHub/[Organizing information with tables] (https://help.github.com/articles/organizing-information-with-tables/)

###Table
| Header | Header | 
| --- | --- |
| Content 1,1 | Content 1,2 xxxxxxxx |
| Content 2,1 etc. | Content 2,2 long form |

###Task List
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

###Code Block
Some basic Git commands are:
```
git status
git add
git commit
```

###Python Code Block
```python
# -*- coding: utf-8 -*-

import models
import wizards
```
###XML Code Block
```XML
<!-- Course Form View -->
        <record model="ir.ui.view" id="view_openacademy_course_form">
            <field name="name">OpenAcademy Course Form View</field>
            <field name="model">openacademy.course</field>
```
###CSV Code Block
```{.table aligns="LCR" caption="This is the **caption**" header="yes"}
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_openacademy_course_user,access_openacademy_course_user,model_openacademy_course,group_openacademy_user,1,0,0,0
access_openacademy_session_user,access_openacademy_session_user,model_openacademy_session,group_openacademy_user,1,0,1,0
```
