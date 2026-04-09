import csv

def csv_para_kml(arquivo_entrada, arquivo_saida):
    # Cabeçalho padrão de um arquivo KML para desenhar uma linha
    kml_header = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Rota Exportada</name>
    <Style id="linhaVermelha">
      <LineStyle>
        <color>ff0000ff</color> <width>4</width> </LineStyle>
    </Style>
    <Placemark>
      <name>Caminho da Rota</name>
      <styleUrl>#linhaVermelha</styleUrl>
      <LineString>
        <extrude>1</extrude>
        <tessellate>1</tessellate>
        <altitudeMode>absolute</altitudeMode>
        <coordinates>
'''
    
    # Fechamento padrão das tags do KML
    kml_footer = '''        </coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>
'''

    try:
        with open(arquivo_entrada, 'r') as csv_file, open(arquivo_saida, 'w') as kml_file:
            leitor_csv = csv.reader(csv_file)
            
            # Escreve o cabeçalho no KML
            kml_file.write(kml_header)
            
            # Itera sobre cada linha do CSV
            for linha in leitor_csv:
                if len(linha) >= 4:
                    # KML exige a ordem: Longitude, Latitude, Altitude
                    latitude = linha[1]
                    longitude = linha[2]
                    altitude = linha[3]
                    
                    # Adiciona a coordenada formatada
                    kml_file.write(f"          {longitude},{latitude},{altitude}\n")
            
            # Escreve o rodapé no KML
            kml_file.write(kml_footer)
            
        print(f"Sucesso! Arquivo '{arquivo_saida}' gerado corretamente.")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executando a função
csv_para_kml('rota.csv', 'rota.kml')