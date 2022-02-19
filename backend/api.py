import random
from fastapi import Request, FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
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

        if (horario1_numberoftags != 0):
          horario1_tagssum = horario1_tagssum / horario1_numberoftags
        if (horario2_numberoftags != 0):
          horario2_tagssum = horario2_tagssum / horario2_numberoftags

        if horario1_tagssum > horario2_tagssum and (len(horario2.get('tags', [])) > 0):
            horarios_to_remove.append(horario2)
        elif horario1_tagssum < horario2_tagssum and (len(horario1.get('tags', [])) > 0):
             horarios_to_remove.append(horario1)
        elif horario1_tagssum == horario2_tagssum and (len(horario1.get('tags', [])) > 0) and (len(horario2.get('tags', [])) > 0):
            #choose random horario and remove it
            if (random.randint(0,1) == 0):
                horarios_to_remove.append(horario1)
            else:
                horarios_to_remove.append(horario2)

    for horario in horarios_to_remove:
      if (horario in horarios):
        horarios.remove(horario)

    return horarios

#return tuples of shedules (eventos) happening at the same time
def colide(shedules):
    colided_events = []
    for i in range(len(shedules)):
        for j in range(i+1, len(shedules)):
            if (colide_horario(shedules[i], shedules[j])):
                colided_events.append((i,j))
    return colided_events


def colide_horario(horario1, horario2):
    #verifica se o horario1 é ao mesmo tempo do horario2
    if (horario1['date_start'] == horario2['date_start'] and horario1['date_end'] == horario2['date_end']):
        return True
    
    #verifica se o horario1 começa antes do horario2 e termina depois dele
    if (horario1['date_start'] < horario2['date_start'] and horario1['date_end'] > horario2['date_start']):
        return True
    
    #verifica se o horario1 começa depois do horario2 e termina antes dele
    if (horario1['date_start'] > horario2['date_start'] and horario1['date_end'] < horario2['date_end']):
        return True

    #verifica se o horario1 começa antes do horario2 e termina depois dele
    if (horario1['date_start'] < horario2['date_start'] and horario1['date_end'] > horario2['date_end']):
        return True

    #verifica se o horario1 começa depois do horario2 e termina antes dele
    if (horario1['date_start'] > horario2['date_start'] and horario1['date_end'] < horario2['date_end']):
        return True

    return False