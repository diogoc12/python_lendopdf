import PyPDF2
import conexao

pdfFile  = open('wpdf.pdf', 'rb')
dadospdf = PyPDF2.PdfFileReader(pdfFile)
qtde1=0
sql=""

for qtde in range(dadospdf.numPages):
       print(dadospdf.getPage(qtde).extractText())
       sql =  sql + str("insert into read_pdf(cidade) VALUES ( '"+dadospdf.getPage(qtde).extractText().replace("'","")+"'); ")
      
conexao.cur.execute(sql)
conexao.cur.execute('select codigo, cidade from read_pdf')
recset = conexao.cur.fetchall()
for rec in recset:
    print(str(rec[0]) + '->' + str(rec[1]))

conexao.con.close()
       

    
    
    
 
