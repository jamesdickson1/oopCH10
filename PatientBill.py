
import PatientClass as p
import ProcedureClass as a


def main():

    iD = 1
    name = "Matt Jones"
    address = "123 Main st, Waco TX 76706"
    phone = "254-555-7415"
    veteran_status = "TRUE"

    pat = p.Patient(iD,name,address,phone,veteran_status)

    #proname,date,pracname,charge,iD
    pro1 = a.Procedure("Physical Exam","2/15/2022","Dr. Irvine",250, 1)
    pro2 = a.Procedure("MRI","2/15/2022","Dr. Hamilton",1500, 1)
    pro3 = a.Procedure("CT Saan","2/17/2022","Dr. Drey", 1200, 2)

    print("*** Patient Bill ***")
    print("Name: ",pat.get_name())
    print("Address: ",pat.get_address())
    print("Phone: ",pat.get_phone())
   
    totcharge = 0
    for i in pro1,pro2,pro3:
        if i.get_iD() == pat.get_iD():
            print("")
            print("Procedure: ", i.get_proname())
            print("Date: ", i.get_date())
            print("Practitioner: ", i.get_pracname())
            print("Charge: $", format(i.get_charge(), ",.2f"))
            print("")
            totcharge += i.get_charge()

    if pat.get_veteran_status() == "TRUE":
        totcharge = 0.6 * totcharge
        print("Total Charges: $",format(totcharge,",.2f"))
    else:
        print("Total Charges: $",format(totcharge,",.2f"))


main()




