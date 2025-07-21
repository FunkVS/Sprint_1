time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_part in time_values.split(','):
    # Разбиваем каждую часть на отдельные компоненты времени
    for component in time_part.split():
        if 'h' in component:
            # Преобразуем часы в минуты
            hours = int(component.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in component:
            # Добавляем минуты
            minutes = int(component.replace('m', ''))
            total_minutes += minutes
        elif 's' in component:
            # Преобразуем секунды в минуты
            seconds = int(component.replace('s', ''))
            total_minutes += seconds // 60

print(f"Общее количество минут: {total_minutes}")