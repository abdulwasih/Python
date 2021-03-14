#importing necessary libraries and modules

from tabula import read_pdf
import pandas as pd
import sqlalchemy


#getting number of pages inside the pdf

from PyPDF2 import PdfFileReader
pdf = PdfFileReader(open('C:\\Users\\user\\Desktop\\samples\\ast_sci_data_tables_sample.pdf','rb'))
#pdf=PdfFileReader(open('file_location','rb'))
numberOfPages=pdf.getNumPages()


#getting all tables inside the pdf into a variable(sometimes,list of tables)

df=read_pdf("C:\\Users\\user\\Desktop\\samples\\ast_sci_data_tables_sample.pdf",pages='all',multiple_tables=True,index=False)
#df=read_pdf("file_location",pages='all',multiple_tables=True,index=False)


#connecting with MySql database
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:@localhost/innovation')
#engine = sqlalchemy.create_engine('mysql+mysqlconnector://username:password@host/databaseName')

#stores each and every tables in the database
for i in range(len(df)):
    dfn=df[i]
    headers=dfn.iloc[0]
    newDf=pd.DataFrame(dfn.values[1:], columns=headers)
    newDf.to_sql(con=engine, name="dftable{}".format(i), if_exists='replace',index=False)
