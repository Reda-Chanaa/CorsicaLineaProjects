import { Component, Inject, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { FormControl, FormGroup } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import * as Highcharts from 'highcharts';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }

  sendStat(File: any): Observable<any> {
    let formData = new FormData();
    formData.append('file1', File, File.name);

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/profiling/', formData, { headers: header })
  }

  sweetviz(File: any): Observable<any> {
    let formData = new FormData();
    formData.append('file1', File, File.name);

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/sweetviz/', formData, { headers: header })
  }

  pandasgui(File: any): Observable<any> {
    let formData = new FormData();
    formData.append('file1', File, File.name);

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/pandasgui/', formData, { headers: header })
  }
  
}
@Component({
  selector: 'app-profiling',
  templateUrl: './profiling.component.html',
  styleUrls: ['./profiling.component.css'],
  providers: [ApiStat]
})
export class ProfilingComponent {

  dataFrame: any;

  value: number;
  df1: any;
  annee: any;
  constructor(private DATACLEANING: ApiStat) {

  }

  // function executed when file is changed
  fileChangeListener1($event: any): void {
    this.df1 = $event.target.files[0]
  }
  
  // Get Statistics forms
  sweetviz() {
    if (this.df1 != null) {
      this.value=0
      this.DATACLEANING.sweetviz(this.df1).subscribe(
        data => {
          this.value=10
          console.log("lets go")
          console.log(data)
          //data=data.substring(15);
          setTimeout(() => {
            //this.router.navigate(['dashboard'], { queryParams: { data: data } });
          }, 1);

        });
    }
  }
  // Get Statistics forms
  profile() {
    if (this.df1 != null) {
      this.value=0
      this.DATACLEANING.sendStat(this.df1).subscribe(
        data => {
          this.value=10
          console.log("lets go")
          console.log(data)
          //data=data.substring(15);
          setTimeout(() => {
            //this.router.navigate(['dashboard'], { queryParams: { data: data } });
          }, 1);

        });
    }
  }

  // Get Statistics forms
  pandasgui() {
    if (this.df1 != null) {
      this.value=0
      this.DATACLEANING.pandasgui(this.df1).subscribe(
        data => {
          this.value=10
          console.log("lets go")
          console.log(data)
          //data=data.substring(15);
          setTimeout(() => {
            //this.router.navigate(['dashboard'], { queryParams: { data: data } });
          }, 1);

        });
    }
  }

}
