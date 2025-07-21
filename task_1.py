time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_part in time_values.split(','):
    for item in time_part.split():
        if 'h' in item:
            hours = int(item.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in item:
            minutes = int(item.replace('m', ''))
            total_minutes += minutes
        elif 's' in item:
            seconds = int(item.replace('s', ''))
            total_minutes += seconds // 60

print(f"Общее количество минут: {total_minutes}")
