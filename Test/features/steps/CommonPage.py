#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import step, then, when


@when("User opens {domain}")
def log_in(context, domain):
    context.common.open(domain)

@then("Types {keyword} in search box")
def search_for(context, keyword):
    context.common.search_for(keyword)
