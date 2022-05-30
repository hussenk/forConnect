import csv
import helpers
from flask import Flask, render_template, request, send_file, send_from_directory, url_for, redirect
from openpyxl import load_workbook
import sys

class service:

    def __init__(self):
        self.arrayData = []

    def getForm(self):
        self.newHeaders = helpers.stringSpelter(request.form['newHeaders'])
        # print(self.newHeaders)
        self.dColumns = helpers.stringSpelter(request.form['dColumns'])
        # print(self.dColumns)

    def handelErrorUpload(self):
        if request.method == 'GET':
            print('request get')
            return False

        if ('upload' not in request.files):
            print('no file')
            return False

        self.file = request.files['upload']
        self.name, self.extension = self.file.filename.rsplit('.', 1)
        if(self.extension != 'xlsx'):
            print('type of file')
            return False

        return True

    def readRows(self):
        self.arrayData = []
        rows = self.ws.iter_rows(2)
        for row in rows:
            data = {}
            for title, cell in zip(self.headers, row):
                data[title] = cell.value
            self.arrayData.append(data)
        # print(row)
        return True

    # set file directory

    def setDirectory(self, directory):
        self.directory = directory
        return True

    def getHeaders(self):
        self.oldHeaders = [cell.value for cell in next(self.ws.rows)]
        return len(self.oldHeaders)

    def loadFile(self):
        # print(self.name)
        wb = load_workbook(self.file)
        self.ws = wb.active
        return True

    def deleteColumn(self):
        self.getHeaders()

        for item in self.dColumns:
            # print(item)
            index = self.oldHeaders.index(item)
            self.ws.delete_cols(index+1)
            self.oldHeaders.remove(item)
        self.setHeaders()
        self.readRows()

    def setHeaders(self):
        count = self.getHeaders()
        # print(count)
        if (request.form.get('newHeadersCB') == 'on' and count == len(self.newHeaders)):
            self.headers = self.newHeaders
        else:
            self.headers = self.oldHeaders
        self.readRows()
        return True

    def saveCsv(self):
        # print(self.arrayData)
        with open(self.directory+'\out.csv', 'w', newline='', encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file,  self.headers)
            dict_writer.writeheader()
            dict_writer.writerows(self.arrayData)

    def download(self):
        print('file?')
        # return send_from_directory(directory=self.directory, filename='out.csv',path=sys.path[0])
        return send_file(self.directory+'\\out.csv', as_attachment=True)
        # print(self.directory)
        # Returning file from appended path
        # return send_from_directory(directory=uploads, filename=filename)
