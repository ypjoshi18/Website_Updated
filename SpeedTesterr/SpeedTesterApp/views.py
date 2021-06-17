from django.shortcuts import render

# Create your views here.
import speedtest
from django.shortcuts import render, redirect


def content(request):
    if request.method == 'POST':
        test = speedtest.Speedtest()
        loading = "Loading Server List.."
        # print("Loading Server List..")
        test.get_servers()
    # print("Choosing Best Server..")
        choosing = "Choosing Best Server.."
        best = test.get_best_server()

        host = best['host']
        country = best['country']
    # print(best)
    # print(f"Found: {best['host']} located in {best['country']}")

        checking = '''Checking Download Speed
                    Checking Upload Speed
                    Calculating Ping'''
    # print("Checking Download Speed")
        download_speed = test.download()
    # print("Checking Upload Speed")
        upload_speed = test.upload()
    # print("Calculating Ping")
        ping_result = test.results.ping

    # print(f"Download Speed: {download_speed / 1024 / 1024} Mbps")
    # print(f"Upload Speed: {upload_speed / 1024 / 1024} Mbps")
    # print(f"Ping: {ping_result} ms")
        output_dict = {'loading': loading,
                    'choosing': choosing,
                    'host': host,
                    'country': country,
                    'download_speed': download_speed / 1024 / 1024,
                    'upload_speed': upload_speed / 1024 / 1024,
                    'ping_result': ping_result}
        return render(request, 'content.html', output_dict)

def index(request):
    return render(request, 'index.html')