from array import array
import PyPDF2
import conexao
from openpyxl import Workbook

wb = Workbook()

planilha = wb.worksheets[0]

pdfFile  = open('Contrato 2.pdf', 'rb')
dadospdf = PyPDF2.PdfFileReader(pdfFile)
informacao=""
posicao=""
for qtde in range(dadospdf.numPages):    
    informacao= informacao + (dadospdf.getPage(qtde).extractText())
    parsed = ''.join(informacao)       

posicao0=informacao.index("SP") 
id = parsed[posicao0-10:posicao0]

posicao1=informacao.index("lavrada em até") 
dias_contrato = parsed[posicao1+15:posicao1+19]

posicao2=informacao.index("3.1. R$") 
valor_contrato = parsed[posicao2+7:informacao.index("4. Da")]

posicao3=informacao.index("São Paulo,") 
data_assinatura = parsed[posicao3+10:posicao3+26]

print(data_assinatura)
	

planilha['A1']='Unit_id'
planilha['B1']='Valor_Total'
planilha['C1']='Data_Contrato'
planilha['D1']='Data_Excritura'

planilha['A2']=id
planilha['B2']=valor_contrato
planilha['C2']=dias_contrato
planilha['D2']=data_assinatura

planilha.title = "OutPutContratos"
wb.save('C:/OutPutContratos.xls')