import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, Injectable, OnInit } from '@angular/core';
import * as Highcharts from "highcharts";
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})

// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }
  getReport(): Observable<any> {

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/report-csc/', { headers: header })
  }
}

@Component({
  selector: 'app-chart-csc',
  templateUrl: './chart-csc.component.html',
  styleUrls: ['./chart-csc.component.css'],
  providers: [ApiStat]
})
export class ChartCscComponent implements OnInit {

  options: any
  data: any
  constructor(private DATACLEANING: ApiStat) {

  }
  ngOnInit() {
    this.getReport()

    this.getOptions(this.data)

    Highcharts.chart('container', this.options)
  }
  getReport = () => {
    this.DATACLEANING.getReport().subscribe(
      data => {
        console.log(data)
        this.data = data;
      },
      error => {
        console.log("error ", error);
      }
    );
  }

  getOptions(data) {
    this.options = {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Report Quotidien CSC'
      },
      subtitle: {
        text: 'Diffusion des écarts'
      },
      xAxis: {
        categories: [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec'
        ],
        crosshair: true
      },
      yAxis: {
        min: -200,
        title: {
          text: 'Ecarts'
        }
      },
      tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
          '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
      },
      plotOptions: {
        column: {
          pointPadding: 0.2,
          borderWidth: 0
        }
      },
      series: [{
        name: '1',
        data: [-49.9, 71.5, 1060.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '2',
        data: [-83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

      }, {
        name: '3',
        data: [-48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 590.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }, {
        name: '4',
        data: [-42.4, 33.2, 34.5, 390.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]

      },
      {
        name: '5',
        data: [-49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '6',
        data: [-83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 830.5, 106.6, 92.3]

      }, {
        name: '7',
        data: [-48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }, {
        name: '8',
        data: [-42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]

      },
      {
        name: '9',
        data: [49.9, 701.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '10',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

      }, {
        name: '11',
        data: [48.9, 38.8, 39.3, 41.4, 407.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 501.2]

      }, {
        name: '12',
        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 390.1, 46.8, 51.1]

      },
      {
        name: '13',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '14',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 830.5, 106.6, 92.3]

      }, {
        name: '15',
        data: [48.9, 38.8, 39.3, 410.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }, {
        name: '16',
        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 390.1, 46.8, 51.1]

      },
      {
        name: '17',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '18',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

      }, {
        name: '19',
        data: [-3, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }, {
        name: '20',
        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, -80, 46.8, 51.1]

      },
      {
        name: '21',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '22',
        data: [83.6, 78.8, 98.5, -40, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

      }, {
        name: '23',
        data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }, {
        name: '24',
        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, -60, 60.4, 47.6, 39.1, 46.8, 51.1]

      },
      {
        name: '25',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '26',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

      }, {
        name: '27',
        data: [-3, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }, {
        name: '28',
        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, -80, 46.8, 51.1]

      },
      {
        name: '29',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

      }, {
        name: '30',
        data: [83.6, 78.8, 98.5, -40, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

      }, {
        name: '31',
        data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

      }]
    }
    return this.options
  }


}
