# -*- coding: utf-8 -*-

from openerp import models, fields, api

<!-- Define Course data model -->
class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    
    <!-- A course has a responsible user. 
    Translates into a Many2one relationship with Resource Users data model -->
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    
    <!-- A course has a one or more sessions. 
    Translates into a One2many relationship with Session data model -->
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
    
<!-- Define Session data model -->    
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    <!-- A session has an instructor. 
    Translates into a Many2one relationship with Resource Partner data model -->
    instructor_id = fields.Many2one('res.partner', string="Instructor", 
        domain=['|', ('instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])
    
    <!-- A session is related to a course. Conversely, a course has one or more sessions. 
    Translates into a Many2one relationship with Course data model -->
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    
    <!-- A session has one or more attendees. An attendee has one or more sessions. 
    Translates into a Many2many relationship with Session data model -->
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
