import psycopg2
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Mensagem



# Create your views here.
def index(request):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="koukce",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ey")

        sql = "select texto, lido from mensagens_mensagem"
        cursor = connection.cursor()

        cursor.execute(sql)
        mensagens = []

        for row in cursor.fetchall():
            mensagens.append(row)

        emp = Mensagem.objects.all()


    except (Exception, psycopg2.Error) as error:
        print("Error while getting data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return render(request, 'mensagens/index.html', {'emp':emp})