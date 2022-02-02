import { Component, ElementRef, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import * as XLSX from 'xlsx';
import { FormControl, FormGroup } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})

// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }
  sendFile(File1: any, File2: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/mesure-csc/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  ID: string;
  NAVIRE: string;
  SENS: string;
  DATE: string;
  HEURE: string;
  NIVEAU: string
  JOUR: string;
  JOURJ: string;
  ECART: string;
}
@Component({
  selector: 'app-mesure-csc',
  templateUrl: './mesure-csc.component.html',
  styleUrls: ['./mesure-csc.component.css'],
  providers: [ApiStat]
})
export class MesureCscComponent {

  dataFrame: any;
  @ViewChild('TABLE') table: ElementRef;
  displayedColumns: string[] = ['ID', 'NAVIRE', 'SENS', 'DATE', 'HEURE', 'NIVEAU', 'JOUR', 'JOURJ', 'ECART'];
  dataSource: MatTableDataSource<StatData>;

  df1: any;
  df2: any;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  constructor(private DATACLEANING: ApiStat) {
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

  deleteData() {
    this.dataSource = new MatTableDataSource([]);
  }
  // function executed when user click on Reporting button
  createFile = () => {
    this.DATACLEANING.sendFile(this.df1, this.df2).subscribe(
      data => {
        this.dataFrame = data;
        // to choose witch data gonna be showing in the table
        this.InitializeVisualization();
        // puts data into the datasource table
        this.dataSource = new MatTableDataSource(data);
        // execute the visualisation function
        this.executeVisualisation();
        // add paginator to the data
        this.dataSource.paginator = this.paginator;
      },
      error => {
        console.log("error ", error);
      }
    );
  }

  //observable for the checkBox execute every time the checkBox is changed
  executeVisualisation() {
    let c0: Observable<boolean> = this.ID.valueChanges;
    let c1: Observable<boolean> = this.NAVIRE.valueChanges;
    let c2: Observable<boolean> = this.SENS.valueChanges;
    let c3: Observable<boolean> = this.DATE.valueChanges;
    let c4: Observable<boolean> = this.HEURE.valueChanges;
    let c5: Observable<boolean> = this.NIVEAU.valueChanges;
    let c6: Observable<boolean> = this.JOUR.valueChanges;
    let c7: Observable<boolean> = this.JOURJ.valueChanges;
    let c8: Observable<boolean> = this.ECART.valueChanges;
    merge(c0, c1, c2, c3, c4, c5,c6,c7,c8).subscribe(v => {
      this.columnDefinitions[0].show = this.ID.value;
      this.columnDefinitions[1].show = this.NAVIRE.value;
      this.columnDefinitions[2].show = this.SENS.value;
      this.columnDefinitions[3].show = this.DATE.value;
      this.columnDefinitions[4].show = this.HEURE.value;
      this.columnDefinitions[5].show = this.NIVEAU.value;
      this.columnDefinitions[6].show = this.JOUR.value;
      this.columnDefinitions[7].show = this.JOURJ.value;
      this.columnDefinitions[8].show = this.ECART.value;
    });
  }
  exportTable() {
    const ws: XLSX.WorkSheet = XLSX.utils.table_to_sheet(this.table.nativeElement);
    const wb: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'CSC');


    let day = new Date().getDate()
    let mois = new Date().getMonth() + 1
    let annee = new Date().getFullYear()
    let date = "MesureCSC_"+ day + "-" + mois + "-" + annee + ".xlsx"
    console.log(date)
    /* save to file */
    XLSX.writeFile(wb, date.toString());
    //TableUtil.exportTableToExcel("reporting", date.toString());

  }
  // to initialize the visualisation with user's checkBox
  InitializeVisualization() {
    this.columnDefinitions = [
      { def: 'ID', label: 'ID', show: this.ID.value },
      { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
      { def: 'SENS', label: 'SENS', show: this.SENS.value },
      { def: 'DATE', label: 'DATE', show: this.DATE.value },
      { def: 'HEURE', label: 'HEURE', show: this.HEURE.value },
      { def: 'NIVEAU', label: 'NIVEAU', show: this.NIVEAU.value },
      { def: 'JOUR', label: 'JOUR', show: this.JOUR.value },
      { def: 'JOURJ', label: 'JOURJ', show: this.JOURJ.value },
      { def: 'ECART', label: 'ECART', show: this.ECART.value }
    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    ID: new FormControl(true),
    NAVIRE: new FormControl(true),
    SENS: new FormControl(true),
    DATE: new FormControl(true),
    HEURE: new FormControl(true),
    NIVEAU: new FormControl(false),
    JOUR: new FormControl(true),
    JOURJ: new FormControl(true),
    ECART: new FormControl(false)
  });

  // geting the checkBox
  ID = this.form.get('ID');
  NAVIRE = this.form.get('NAVIRE');
  SENS = this.form.get('SENS');
  DATE = this.form.get('DATE');
  HEURE = this.form.get('HEURE');
  NIVEAU = this.form.get('NIVEAU')
  JOUR = this.form.get('JOUR');
  JOURJ = this.form.get('JOURJ');
  ECART = this.form.get('ECART')

  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'ID', label: 'ID', show: this.ID.value },
    { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
    { def: 'SENS', label: 'SENS', show: this.SENS.value },
    { def: 'DATE', label: 'DATE', show: this.DATE.value },
    { def: 'HEURE', label: 'HEURE', show: this.HEURE.value },
    { def: 'NIVEAU', label: 'NIVEAU', show: this.NIVEAU.value },
    { def: 'JOUR', label: 'JOUR', show: this.JOUR.value },
      { def: 'JOURJ', label: 'JOURJ', show: this.JOURJ.value },
      { def: 'ECART', label: 'ECART', show: this.ECART.value }
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }

}
