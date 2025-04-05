import json

def thay_doi_gia_tri(api_text_file):

    with open (api_text_file, 'r') as file:

        data = json.load(file)

        for person in data["results"]:
            # Lấy thông tin giới tính
            gioi_tinh_goc = person.get("gender","unknwon")
            gioi_tinh_thay_doi = person.get("gender","unknwon")

            if gioi_tinh_thay_doi.lower() == "female":
                gioi_tinh_thay_doi = "male"
            elif gioi_tinh_thay_doi.lower() == "male":
                gioi_tinh_thay_doi = "female"


            print(f"{gioi_tinh_goc= }\n{gioi_tinh_thay_doi= }")
            """
            OUTPUT: print(f"{gioi_tinh_goc= }\n{gioi_tinh_thay_doi= }")
            gioi_tinh_goc= 'female'
            gioi_tinh_thay_doi= 'male' 
            """