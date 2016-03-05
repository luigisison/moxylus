# -*- coding: utf-8 -*-

<!-- Enable calendar view -->
from datetime import timedelta

from openerp import models, fields, api, exceptions

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
    
    <!-- Define a duplicate name option. -->
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)
    
    <!-- Check that the course title and the course description are different. -->
     _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        <!-- Make the course name unique. -->
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
    
<!-- Define Session data model -->    
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    
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
    
    <!-- Calculate number of taken seats --> 
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    end_date = fields.Date(string="End Date", store=True,
        compute='_get_end_date', inverse='_set_end_date')
        
    <!-- Calculate Session duration in hours -->
    hours = fields.Float(string="Duration in hours",
                         compute='_get_hours', inverse='_set_hours')    

    <!-- Calculate percentage of taken seats -->
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
    
    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24
            
    <!-- Warn about invalid values for taken seats -->
    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    <!-- Add calendar view to the Session model -->
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1

    <!-- Check that the instructor is not an attendee in their own class -->
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")
                
<!-- Model template -->
# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
