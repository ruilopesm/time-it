from fastapi import Request, FastAPI

app = FastAPI()

"""
{
  "horario": [
    {
      "title": "Artic Monkeys",
      "date_start": "30000",
      "date_end": "100000",
      "tags": [
        "vibes"
      ]
    },
    {
      "title": "Artista523",
      "date_start": "30000",
      "date_end": "50000",
      "tags": [
        "rock",
        "metal"
      ]
    },
    {
      "title": "Teste12453643",
      "date_start": "110000",
      "date_end": "140000",
      "tags": [
        "rock",
        "metal"
      ]
    },
    {
      "title": "Lol213457654",
      "date_start": "160000",
      "date_end": "170000",
      "tags": [
        "rock",
        "metal"
      ]
    }
  ],
  "interesses": {
    "tags": {
        "rock": "1",
        "metal": "5",
        "vibes": "2"
      }
  }
}
"""

@app.get('/')
async def home(request: Request):
    json_data = await request.json()

    horarios = json_data['horario']
    interesses = json_data['interesses']
    tags = interesses['tags']
    
    horarios_to_remove = []
    colided_events = colide(horarios) # retorna uma lista de tuplos de eventos que coincidem no horario

    for event in colided_events:
        horario1 = horarios[event[0]]
        horario1_tagssum = 0
        horario1_numberoftags = 0

        horario2 = horarios[event[1]]
        horario2_tagssum = 0
        horario2_numberoftags = 0

        for htags in horario1.get('tags', []):
            horario1_numberoftags += 1
            horario1_tagssum += int(tags[htags])
        for htags in horario2.get('tags', []):
            horario2_numberoftags += 1
            horario2_tagssum += int(tags[htags])

        horario1_tagssum = horario1_tagssum / horario1_numberoftags
        horario2_tagssum = horario2_tagssum / horario2_numberoftags

        if horario1_tagssum > horario2_tagssum:
            horarios_to_remove.append(horario2)
        else:
             horarios_to_remove.append(horario1)

    for horario in horarios_to_remove:
      if (horario in horarios):
        horarios.remove(horario)

    return horarios

#return tuples of shedules (eventos) happening at the same time
def colide(shedules):
    colidiu = []
    for i in range(len(shedules)):
        for j in range(len(shedules)):
            if i != j:
                if colide_horario(shedules[i], shedules[j]):
                    colidiu.append((i,j))
    return colidiu

def colide_horario(horario1, horario2):
    return horario1['date_start'] <= horario2['date_start'] <= horario1['date_end'] or horario1['date_start'] <= horario2['date_end'] <= horario1['date_end']
