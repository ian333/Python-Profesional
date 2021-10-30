from datetime import date, datetime
import pytz


if __name__ == "__main__":
    bogota_timezone= pytz.timezone("America/Bogota")
    bogota_date=datetime.now(bogota_timezone)
    print("Bogota: ",bogota_date.strftime("%d/%m/%Y , %H:%M;%S"))

    mexico_timezone= pytz.timezone("America/Mexico_City")
    mexico_date=datetime.now(mexico_timezone)
    print("CDMX: ",bogota_date.strftime("%d/%m/%Y , %H:%M;%S"))

    caracas_timezone= pytz.timezone("America/Caracas")
    caracas_date=datetime.now(caracas_timezone)
    print("Bogota: ",caracas_date.strftime("%d/%m/%Y , %H:%M;%S"))
