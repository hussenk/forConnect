from turtle import st
from unicodedata import name
from flask import Flask, render_template, request, url_for, redirect

class serves:

    def __init__(self):
        pass
    
    def stringSpelter(self,str):
      return str.replace(';',' ').replace(',',' ').replace('.',' ').replace('،',' ').replace('-',' ').split()



    def handelErrorUpload(self):
        # check method
        # print('check  request method')
        if(request.method== 'GET'):
            return redirect('/')
        # check if file exist
        # print('check if file exist')
        if ('upload' not in request.files):
            return redirect('/')

        self.dColumns = self.stringSpelter(request.form['dColumns'])
        self.newHeaders = self.stringSpelter(request.form['newHeaders'])
        # print(self.dColumns)
        print(self.newHeaders)
        self.file = request.files['upload']
        
        # getting file name and extension
        self.name,  self.extension =  self.file.filename.rsplit('.',1)
        print('getting file name and extension')

        # check type file 
        # print('check type file')   
        if(self.extension != 'xlsx'):
            return redirect('/')

    def handelFile():
        pass


    def deleteColumn(self):
        for item in self.dColumns:
            index = headers.index(item)
            ws.delete_cols(index+1)
            headers.remove(item)

    def getOldHeaders():
        pass
    