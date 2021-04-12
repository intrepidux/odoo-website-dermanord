# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Webshop Dermanord',
    'version': '1.0',
    'category': '',
    'summary': '',
    'description': """
Special layout for Dermanord AB webshop
====================
""",
    'author': 'Vertel AB',
    'license': 'AGPL-3',
    'website': 'http://www.vertel.se',
    'depends': [
        'portal',
        'product_multi_image_attachment',
        'website_sale_product_gallery',
        'website_blog',
        'product_dermanord',
        'product_private',
        'website_sale_previous_products',
        'website_sale_terms',
        'website_sale_comment',
        'website_product_pcategory',
        'website_imagemagick',
        'product_ingredients',
        'product_facets',
        'website_bootstrap_select2',
        'website_fts_product',
        'website_fts_popular',
        'product_attribute_value_image',
        'website_sale_instock',
        'website_sale_lang_pricelist',
        'crm_campaign_phase_default_variant',
        'website_sale_delivery',
        'website_sale_minimum_order_value',
        'website_sale_price_chart',
        'calc_orderpoint',
        'reseller_dermanord',
        'mrp_dermanord',
        'website_translate_extra_modules',
        'product_pricelist_dermanord',
        'delivery',
        ],
    'data': [
        'views/webshop_dermanord_view.xml',
        'views/website_sale_view.xml',
        'views/template_checkout.xml',
        'views/filter_sort_modal.xml',
        'data/webshop_dermanord_data.xml',
        'views/product_view.xml',
        'security/dn_security.xml',
        'security/ir.model.access.csv',
        'views/stock_notification_view.xml',
        # ~ 'data/warehouse_data.xml',
    ],
    'qweb': ['static/src/xml/product.xml'],
    'application': False,
}

