import sys
sys.path.insert(0, "../core")
from core import cyl_transpose_logic as ctl
from core import power_at_logic as pal
from core import mf_to_sv_logic as msl
from core import format
from flask import Flask, render_template, request

#Create app
app = Flask(__name__)

#App route for homepage.
@app.route('/')
def home():
    return render_template('index.html')

#App route for Cyl Transposition Page
@app.route('/cyl_transpose', methods=['GET','POST'])
def cyl_transpose():
    #Initialize variables used by template.
    original_rx_formatted_od = None
    original_rx_formatted_os = None
    rx_formatted_od = None
    rx_formatted_os = None
    invalid_entry = False

    #When user submits form...
    if request.method == 'POST':

        #Format values entered by user, and validate entry.
        rx_vals = format.get_vals(request, "sv")
        if format.validate_entry(rx_vals, "sv"):
            #If entry is valid...
            #Format original rx entered to display above result. Split into OD and OS.
            invalid_entry = False
            original_rx_formatted = format.format_rx(format.entry_consolidate(rx_vals, "sv"), "sv")
            original_rx_formatted_od = original_rx_formatted[0]
            original_rx_formatted_os = original_rx_formatted[1]

            #Perform conversion, and format result.
            rx_converted = ctl.cyl_convert(rx_vals, request.form.get('convert_type'))
            rx_formatted = format.format_rx(rx_converted, "sv")
            rx_formatted_od = rx_formatted[0]
            rx_formatted_os = rx_formatted[1]
        else:
            #If entry is invalid, set invalid_entry var to True.
            invalid_entry = True

    return render_template('cyl_transpose.html',
                           original_rx_formatted_od=original_rx_formatted_od,
                           original_rx_formatted_os=original_rx_formatted_os,
                           rx_formatted_od=rx_formatted_od,
                           rx_formatted_os=rx_formatted_os,
                           invalid_entry=invalid_entry)

#App route for Power At 90/180 Page.
@app.route('/power_at', methods=['GET','POST'])
def power_at():
    #Initialize variables used by template.
    original_rx_formatted_od = None
    original_rx_formatted_os = None
    power_result_od = None
    power_result_os = None
    power_selected = None
    invalid_entry = False

    #When user submits form...
    if request.method == 'POST':

        #Format values entered by user, and validate entry.
        rx_vals = format.get_vals(request, "sv")
        if format.validate_entry(rx_vals, "sv"):
            #If entry is valid...
            #Format original rx entered to display above result. Split into OD and OS.
            invalid_entry = False
            original_rx_formatted = format.format_rx(format.entry_consolidate(rx_vals, "sv"), "sv")
            original_rx_formatted_od = original_rx_formatted[0]
            original_rx_formatted_os = original_rx_formatted[1]

            #Perform power calculation.
            power_result = pal.power_at(rx_vals, int(request.form.get('power')))
            power_result_od = power_result[0]
            power_result_os = power_result[1]
            power_selected = request.form.get('power')
        else:
            #If entry is invalid, set invalid_entry var to True.
            invalid_entry = True

    return render_template("power_at.html",
                           original_rx_formatted_od=original_rx_formatted_od,
                           original_rx_formatted_os=original_rx_formatted_os,
                           power_result_od=power_result_od,
                           power_result_os=power_result_os,
                           power_selected=power_selected,
                           invalid_entry=invalid_entry)

#App route for Multifocal to Single Vision page.
@app.route('/mf_to_sv', methods=['GET','POST'])
def mf_to_sv():
    #Initialize variables used by template.
    original_rx_formatted_od = None
    original_rx_formatted_os = None
    rx_formatted_od = None
    rx_formatted_os = None
    invalid_entry = False

    #When user submits form...
    if request.method == 'POST':

        #Format values entered by user, and validate entry.
        rx_vals = format.get_vals(request, "mf")
        if format.validate_entry(rx_vals, "mf"):
            #If entry is vald...
            #Format original rx entered to display above result. Split into OD and OS.
            invalid_entry = False
            original_rx_formatted = format.format_rx(format.entry_consolidate(rx_vals, "mf"), "mf")
            original_rx_formatted_od = original_rx_formatted[0]
            original_rx_formatted_os = original_rx_formatted[1]

            #Perform conversion and format result.
            rx_converted = msl.mf_to_sv(rx_vals, request.form.get('convert_type'))
            rx_formatted = format.format_rx(rx_converted, "sv")
            rx_formatted_od = rx_formatted[0]
            rx_formatted_os = rx_formatted[1]
        else:
            #If entry is invalid, set invalid_entry var to True.
            invalid_entry = True

    return render_template("mf_to_sv.html",
                           original_rx_formatted_od=original_rx_formatted_od,
                           original_rx_formatted_os=original_rx_formatted_os,
                           rx_formatted_od=rx_formatted_od,
                           rx_formatted_os=rx_formatted_os,
                           invalid_entry=invalid_entry)

if __name__ == '__main__':
    app.run(debug=False)