odoo.define('custom_dashboard.DashboardRewrite', function (require) {
"use strict";

const ActionMenus = require('web.ActionMenus');
const ComparisonMenu = require('web.ComparisonMenu');
const ActionModel = require('web/static/src/js/views/action_model.js');
const FavoriteMenu = require('web.FavoriteMenu');
const FilterMenu = require('web.FilterMenu');
const GroupByMenu = require('web.GroupByMenu');
const patchMixin = require('web.patchMixin');
const Pager = require('web.Pager');
const SearchBar = require('web.SearchBar');
const { useModel } = require('web/static/src/js/model.js');

const { Component, hooks } = owl;

var concurrency = require('web.concurrency');
var config = require('web.config');
var field_utils = require('web.field_utils');
var time = require('web.time');
var utils = require('web.utils');
var AbstractAction = require('web.AbstractAction');
var ajax = require('web.ajax');
var Dialog = require('web.Dialog');
var field_utils = require('web.field_utils');
var core = require('web.core');
var rpc = require('web.rpc');
var session = require('web.session');
var web_client = require('web.web_client');
var abstractView = require('web.AbstractView');
var _t = core._t;
var QWeb = core.qweb;

const { useRef, useSubEnv } = hooks;


var HrDashboard = AbstractAction.extend({

    template: 'CustomDashboardMain',
    cssLibs: [
        '/custom_dashboard/static/src/css/lib/nv.d3.css'
    ],
    jsLibs: [
        '/custom_dashboard/static/src/js/lib/d3.min.js'
    ],

     events: {
            'click .my_leave_request':'my_leave_request',
            'click .request_sale_orders':'request_sale_orders',
            'click .request_contacts':'request_contacts',
            'click .request_invoices':'request_invoices',
            'click .request_borrowings':'request_borrowings',
            'click .request_planning':'request_planning',
            'click .request_documents':'request_documents',
            'click .request_purchases':'request_purchases',
            'click .request_projects':'request_projects',
            "click .o_hr_attendance_sign_in_out_icon": function() {
            this.$('.o_hr_attendance_sign_in_out_icon').attr("disabled", "disabled");

        },
        'click #broad_factor_pdf': 'generate_broad_factor_report',


    },



    init: function(parent, context) {

        this._super(parent, context);
        this.date_range = 'week';  // possible values : 'week', 'month', year'
        this.date_from = moment().subtract(1, 'week');
        this.date_to = moment();
        this.dashboards_templates = ['LoginEmployeeDetails','ManagerDashboard', 'EmployeeDashboard'];
        this.employee_birthday = [];
        this.upcoming_events = [];
        this.announcements = [];
        this.login_employee = [];

    },

    willStart: function(){
        var self = this;
        this.login_employee = {};
        return this._super()
        .then(function() {
            var def0 =  self._rpc({
                    model: 'hr.employee',
                    method: 'check_user_group'
            }).then(function(result) {
                if (result == true){
                    self.is_manager = true;
                }
                else{
                    self.is_manager = false;
                }
            });
            var def1 =  self._rpc({
                    model: 'custom.dashboard',
                    method: 'get_custom_info'
            }).then(function(result) {
                console.log("==============result1==================",result)
                console.log("==============result1========0==========",result[0])
                self.employee_data =  result;
            });
        return $.when(def0, def1);
        });
    },

    start: function() {
            console.log("START FUNCTION")
            var self = this;
            this.set("title", 'Dashboard');
            return this._super().then(function() {
                self.update_cp();
                self.render_dashboards();
                self.$el.parent().addClass('oe_background_grey');
            });
        },

    fetch_data: function() {
        var self = this;
        var def0 =  self._rpc({
                model: 'hr.employee',
                method: 'check_user_group'
        }).then(function(result) {
            if (result == true){
                self.is_manager = true;
            }
            else{
                self.is_manager = false;
            }
        });
        var def1 =  this._rpc({
                model: 'custom.dashboard',
                method: 'get_custom_info'
        }).then(function(result) {
            console.log("==============result2==================",result)
            console.log("==============result2========0==========",result[0])
            self.employee_data =  result;
        });

        return $.when(def0, def1);
    },

    render_dashboards: function() {
        var self = this;
        console.log("===============self====================",self)
        if (this.login_employee){
            var templates = []
            if( self.is_manager == true){templates = ['LoginEmployeeDetails','ManagerDashboard', 'EmployeeDashboard'];}
            else{ templates = ['LoginEmployeeDetails', 'EmployeeDashboard'];}
            _.each(templates, function(template) {
                self.$('.o_hr_dashboard').append(QWeb.render(template, {widget: self}));
            });
        }
        else{
                self.$('.o_hr_dashboard').append(QWeb.render('EmployeeWarning', {widget: self}));
            }
    },

    on_reverse_breadcrumb: function() {console.log("ON_REVERSE_BREADCRUMB")
        var self = this;
        web_client.do_push_state({});
        this.update_cp();
        this.fetch_data().then(function() {
            self.$('.o_hr_dashboard').empty();
            self.render_dashboards();
        });
    },

    my_leave_request: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("My Leave Request"),
                type: 'ir.actions.act_window',
                res_model: 'hr.leave',
                view_mode: 'tree,form,calendar',
                views: [[false, 'list'],[this.employee_data.my_leave_request_form_id, 'form']],
                domain: [['employee_id','=', this.employee_data.employee_id],['state','=','confirm']],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_sale_orders: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Requested Sale Orders"),
                type: 'ir.actions.act_window',
                res_model: 'sale.order',
                view_mode: 'tree,kanban,form,calendar',
                views: [[false, 'list'],[false, 'kanban'],[false, 'calendar'],[false, 'form']],
                domain: [['state','=','waiting_for_approval']],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_contacts: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Requested Contacts"),
                type: 'ir.actions.act_window',
                res_model: 'res.partner',
                view_mode: 'tree,kanban,form',
                views: [[false, 'list'],[false, 'kanban'],[false, 'form']],
                domain: [['state','=','waiting_approval']],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_invoices: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Invoices"),
                type: 'ir.actions.act_window',
                res_model: 'account.move',
                view_mode: 'tree,kanban,form',
                views: [[false, 'list'],[false, 'kanban'],[false, 'form']],
                domain: [['move_type','=','out_invoice']],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_borrowings: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Borrowings"),
                type: 'ir.actions.act_window',
                res_model: 'borrow.borrow',
                view_mode: 'tree,form',
                views: [[false, 'list'],[false, 'form']],
                domain: [],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_planning: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Planning"),
                type: 'ir.actions.act_window',
                res_model: 'planning.slot',
                view_mode: 'gantt,tree,form,calendar,kanban',
                views: [[false, 'gantt'],[false, 'calendar'],[false, 'list'],[false, 'kanban'],[false, 'form']],
                domain: [['employee_id','=', this.employee_data.employee_id]],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_documents: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Documents"),
                type: 'ir.actions.act_window',
                res_model: 'document.document',
                view_mode: 'kanban,tree,form',
                views: [[false, 'kanban'],[false, 'list'],[false, 'form']],
                domain: [],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_purchases: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Purchase Orders"),
                type: 'ir.actions.act_window',
                res_model: 'purchase.order',
                view_mode: 'tree,kanban,calendar,form',
                views: [[false, 'list'],[false, 'kanban'],[false, 'calendar'],[false, 'form']],
                domain: [],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    request_projects: function(ev){
        var self = this;
        ev.stopPropagation();
        ev.preventDefault();

        var options = {
            on_reverse_breadcrumb: this.on_reverse_breadcrumb,
        };
        if(this.employee_data.employee_id){
            this.do_action({
                name: _t("Projects"),
                type: 'ir.actions.act_window',
                res_model: 'project.project',
                view_mode: 'kanban,tree,form',
                views: [[false, 'kanban'],[false, 'list'],[false, 'form']],
                domain: [],
                target: 'current' //self on some of them
            }, {
                    on_reverse_breadcrumb: this.on_reverse_breadcrumb
            });
        }
    },

    update_cp: function() {
        var self = this;
    },

   });

    core.action_registry.add('custom_dashboard', HrDashboard);

return HrDashboard;

});