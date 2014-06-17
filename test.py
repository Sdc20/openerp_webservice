#!/usr/bin/python
# -*- coding: utf-8 -*-

import xmlrpclib
 
user = 'admin'
pwd = 'faisal'
dbname = 'new_one'
model = 'webservice.core.methods'
 
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock.login(dbname ,user ,pwd)
data = 1
 
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
partner_data = {'name':u'cliché kosten', 'customer':True,}
partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner_data)
print partner_id


# journal_data = sock.execute(dbname, uid, pwd, model, 'get_journals_company_wise', data)

# print journal_data
# accounts_data = sock.execute(dbname, uid, pwd, model, 'get_accounts_company_wise', data)
# print accounts_data

# currency_data = sock.execute(dbname, uid, pwd, model, 'get_currencies_company_wise', data)
# print currency_data

# tax_data = sock.execute(dbname, uid, pwd, model, 'get_accounts_taxes_company_wise', data)
# print tax_data
# invoice_data = {
# 				'account_id':40,
#                'partner_id':6,
#                 'fiscal_position':False,
#                 'date_invoice':False,
#                 'journal_id':11,
#                 'comment':False,
#                 'date_due':False,
#                 'origin':'123123',
#                 'supplier_invoice_number':'1212323234444',
#                 'type':'out_invoice',
#                 'invoice_line_data':'product_id:49?name:[ADPT] USB Adapterxxxx?account_id:51?account_analytic_id:False?discount:0?price_unit:18?quantity:1?invoice_tax_id:1+7;product_id:17?name:[C-Case] Computer Case?account_id:51?account_analytic_id:False?discount:0?price_unit:25?quantity:1?invoice_tax_id:1+7'
#                 }
# invoice_id = sock.execute(dbname, uid, pwd, model, 'create_invoice', invoice_data)
# print invoice_id




#===============================================================================
# data_dictionary = {'company_id':4,'field_name':'name', 'field_value':'c2_faisal','partner_type':'customer'}
# partner_id = sock.execute(dbname, uid, pwd, model, 'query_partner_company_wise', data_dictionary)
# journal_dictionary = {'company_id':4, 'journal_name':'bank'}
# journal_id = sock.execute(dbname, uid, pwd, model, 'query_journal_company_wise', journal_dictionary)
# print journal_id
# 
# # CREATE A PARTNER
# data = [4, 'name', 'c2_faisal', 'customer']
# partner_data = {'name':'Kashif4', 'company_id':4, 'customer':True}
# product_data = {'name':'ddd_ppp_created_by_faisal13355','company_id':4}
# journal_data = [4, 'bank']
# partner_id = sock.execute(dbname, uid, pwd, model, 'query_partner_company_wise', data)
# print partner_id
# #product_id = sock.execute(dbname, uid, pwd, model, 'create_product', product_data) 
# journal_id = sock.execute(dbname, uid, pwd, model, 'query_journal_company_wise', journal_data)
# #def query_journal_company_wise(self, cr, uid, data, context=None):
# invoice_data = {
#                'partner_id':11,
#                 'fiscal_position':False,
#                 'date_invoice':False,
#                 'journal_id':25,
#                 'comment':False,
#                 'date_due':False,
#                 'origin':'123123',
#                 'supplier_invoice_number':'1212323234444',
#                 'type':'out_invoice',
#                 'invoice_line_data':'product_id:14?name:[ADPT] USB Adapterxxxx?account_id:71?account_analytic_id:False?discount:0?price_unit:18?quantity:1'
#                 }
# invoice_id = sock.execute(dbname, uid, pwd, model, 'create_invoice', invoice_data)
# print invoice_id
#===============================================================================






