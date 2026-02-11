
def load_log_file(path):
    with open(path) as file:
        lines = file.readlines()
    return lines    


def extract_lines(lines):
    all_lines = []
    for line in lines:
        words = line.strip().split()
        all_lines.append(words)    

    return all_lines    
    
def parse_log_data(lines):
    LogData = {}
    for item in lines:
        status = item[2]
        message = " ".join(item[3:])
        if status not in LogData:
            LogData[status] = {"count": 0, "message": []}

        LogData[status]["count"] += 1
        LogData[status]["message"].append(message)

    return LogData  
        

def print_summary(LogData):
    total_count = sum(LogData[status]["count"] for status in LogData)
    print("Total lines:", total_count)

    for status in LogData:
        print(status, ":", LogData[status]["count"])

    if "ERROR" in LogData:
        print("Errors:")
        for msg in LogData["ERROR"]["message"]:
            print(" -", msg)


if __name__ == '__main__':
    file = load_log_file('app.log')
    lines = extract_lines(file)
    LogData = parse_log_data(lines)
    print_summary(LogData)
    
    
                    
        
