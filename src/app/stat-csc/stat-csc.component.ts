import { Component, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
@Injectable({
  providedIn: 'root'
})
// class pour les requettes GET et POST.
export class ApiStandartization {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }

  sendFile(File1: any, File2:any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/table-list/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  CORSE: string;
  CIBLE: string;
  VENTE: string;
  CUMUL: string;
  BUDGET: string;
}
@Component({
  selector: 'app-stat-csc',
  templateUrl: './stat-csc.component.html',
  styleUrls: ['./stat-csc.component.css'],
  providers: [ApiStandartization]
})
export class StatCscComponent {

  HiddenJan = false
  HiddenFev = false
  HiddenMar = false
  HiddenAvr = false
  HiddenMai = false
  HiddenJuin = false
  HiddenJuil = false
  HiddenAout = false
  HiddenSep = false
  HiddenOct = false
  HiddenNov = false
  HiddenDec = false
  renderedData: any;
  dataFrame: any;

  displayedColumns: string[] = ['CORSE', 'CIBLE', 'VENTE', 'CUMULE', 'BUDGET'];
  dataSource: MatTableDataSource<StatData>;

  @ViewChild(MatPaginator) paginator: MatPaginator;

  janvier = new FormControl('');
  fevrier = new FormControl('');
  mars = new FormControl('');
  avril = new FormControl('');
  mai = new FormControl('');
  juin = new FormControl('');
  juillet = new FormControl('');
  aout = new FormControl('');
  septembre = new FormControl('');
  octobre = new FormControl('');
  novembre = new FormControl('');
  decembre = new FormControl('');

  Cjanvier = new FormControl('');
  Cfevrier = new FormControl('');
  Cmars = new FormControl('');
  Cavril = new FormControl('');
  Cmai = new FormControl('');
  Cjuin = new FormControl('');
  Cjuillet = new FormControl('');
  Caout = new FormControl('');
  Cseptembre = new FormControl('');
  Coctobre = new FormControl('');
  Cnovembre = new FormControl('');
  Cdecembre = new FormControl('');

  element: any;
  df1: any;
  df2: any;
  value: number;

  constructor(private DATACLEANING: ApiStandartization, private router: Router, fb: FormBuilder) {

    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource([]);

  }

  // function executed when file is changed
  fileChangeListener1($event: any): void {
    this.df1 = $event.target.files[0]
  }
  // function executed when file is changed
  fileChangeListener2($event: any): void {
    this.df2 = $event.target.files[0]
  }

  // function executed when user click on standardize button
  createFile = () => {
    if (this.df1 != null && this.df2 != null) {
      this.value = 0
      this.DATACLEANING.sendFile(this.df1,this.df2).subscribe(
        data => {
          this.value = 10
          this.dataFrame = data;
          // to choose witch data gonna be showing in the table
          this.InitializeVisualization();
          // puts data into the datasource table
          this.dataSource = new MatTableDataSource(data);
          // execute the visualisation function
          this.executeVisualisation();
          // put Data into a rendered Data to export
          this.dataSource.connect().subscribe(d => this.renderedData = d);
          // add paginator to the data
          this.dataSource.paginator = this.paginator;
        },
        error => {
          console.log("error ", error);
        }
      );
    }

  }

  //observable for the checkBox execute every time the checkBox is changed
  executeVisualisation() {
    let c0: Observable<boolean> = this.CORSE.valueChanges;
    let c1: Observable<boolean> = this.INB.valueChanges;
    let c2: Observable<boolean> = this.EXTB.valueChanges;
    let c3: Observable<boolean> = this.POI.valueChanges;
    let c4: Observable<boolean> = this.BUDGET.valueChanges;
    merge(c0, c1, c2, c3, c4).subscribe(v => {
      this.columnDefinitions[0].show = this.CORSE.value;
      this.columnDefinitions[1].show = this.INB.value;
      this.columnDefinitions[2].show = this.EXTB.value;
      this.columnDefinitions[3].show = this.POI.value;
      this.columnDefinitions[4].show = this.BUDGET.value;
    });
  }

  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'CORSE', label: 'CORSE', show: this.CORSE.value },
      { def: 'CIBLE', label: 'CIBLE', show: this.INB.value },
      { def: 'VENTE', label: 'VENTE', show: this.EXTB.value },
      { def: 'CUMUL', label: 'POI', show: this.POI.value },
      { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    CORSE: new FormControl(true),
    CIBLE: new FormControl(true),
    VENTE: new FormControl(true),
    CUMUL: new FormControl(true),
    BUDGET: new FormControl(true)
  });

  // geting the checkBox
  CORSE = this.form.get('CORSE');
  INB = this.form.get('CIBLE');
  EXTB = this.form.get('VENTE');
  POI = this.form.get('CUMUL');
  BUDGET = this.form.get('BUDGET')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'CORSE', label: 'CORSE', show: this.CORSE.value },
    { def: 'CIBLE', label: 'CIBLE', show: this.INB.value },
    { def: 'VENTE', label: 'VENTE', show: this.EXTB.value },
    { def: 'CUMUL', label: 'POI', show: this.POI.value },
    { def: 'BUDGET', label: 'BUDGET', show: this.BUDGET.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }
}

