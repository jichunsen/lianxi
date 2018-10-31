import requests



session=requests.session()
session.get("https://www.lagou.com/")
session.get("https://www.lagou.com/jobs/list_python")

res=session.post("https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false",
                  headers={

                            "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
                            "X-Anit-Forge-Code": "0",
                            "X-Anit-Forge-Token": None,
                            "X-Requested-With": "XMLHttpRequest",
                            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

                  },
                  data={
                    "first": "true",
                    "pn":1,
                    "kd":"python",
                  }
                  )


print(res.text)

