import { Component, Inject, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { FormArray, FormBuilder, FormControl, FormGroup } from '@angular/forms';

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

  getcolumn(File: any): Observable<any>{
    let formData = new FormData();
    formData.append('file1', File, File.name);

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/getcolumn/', formData, { headers: header })
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
  values: number;
  df1: any;
  annee: any;
  form: FormGroup;
  ordersData = [];


  constructor(private DATACLEANING: ApiStat) {

  }
  
  // function executed when file is changed
  fileChangeListener1($event: any): void {
    this.df1 = $event.target.files[0]
    this.values=0
    this.DATACLEANING.getcolumn(this.df1).subscribe(
      data => {
        this.values=10
        // async orders
        this.ordersData=data
        console.log(data)
      }
    )
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
