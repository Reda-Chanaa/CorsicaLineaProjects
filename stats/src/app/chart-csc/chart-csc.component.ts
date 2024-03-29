import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, Injectable, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import * as Highcharts from "highcharts";
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})

// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = environment.BASE_URL;

  constructor(private http: HttpClient) {

  }
  getReport(annee:any): Observable<any> {

    let formData = new FormData();
    formData.append('annee', annee);
    console.log(formData)
    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/report-csc/', formData, { headers: header })
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
  Fannee = new FormControl('');
  annee :any
  value: number=10;
  constructor(private DATACLEANING: ApiStat) {
    
  }
  changed(value) {
    this.annee = value.target.value
  }

  ngOnInit() {
    
  }

  async getReport(){
    this.value=0
    this.DATACLEANING.getReport(this.annee).subscribe(
      data => {
        this.value=10
        this.data = data;
        console.log(data[0])
        this.getOptions(this.data)
        Highcharts.chart('container', this.options)
      },
      error => {
        console.log("error ", error);
      }
    );
  }

  async dashboard(){
    await this.getReport()
  }

  async getOptions(data:any) {
    var df=[]
    console.log(data.length)
    for (let index = 0; index < data.length; index++) {
      var series1 = {
      name: 0,
      data: []
    }
    series1.name=index+1;
      series1.data=[Number(data[index].Jan), Number(data[index].Feb), Number(data[index].Mar), Number(data[index].Apr), Number(data[index].May), Number(data[index].Jun), Number(data[index].Jul), Number(data[index].Aug), Number(data[index].Sep), Number(data[index].Oct), Number(data[index].Nov), Number(data[index].Dec)]
      df.push(series1)
    }
    console.log(df)

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
          '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
      },
      plotOptions: {
        column: {
          pointPadding: 0.2,
          borderWidth: 0.01
        }
      },
      series: df
    }
    return this.options
  }


}
