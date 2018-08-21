#!/usr/bin/python

import openshift as oc
from openshift.model import Missing
import traceback

with oc.tracker() as t:
    with oc.client_host(hostname="18.222.71.125", username="root", auto_add_host=True):  # free-stg
        with oc.project("openshift-monitoring"):
            try:
                cr_rules = oc.selector("prometheusrules")
                print("CR has the following rule sets: {}".format(cr_rules.qnames()))

                if cr_rules.object().model.metadata.labels.cr_generated is Missing:
                    print("Rule was not generated by CR")

                oc.selector('pods').annotate(annotations={
                    'cr_annotation_test': None,
                })
                #cr_rules.object().label({
                #    'cr_test': 'yes',
                #})

                print("Result:\n{}".format(t.get_result()))
            except Exception:
                traceback.print_exc()



