import { Component, ElementRef, Inject, ViewChild } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { merge, Observable } from 'rxjs';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import * as Highcharts from 'highcharts';
import * as XLSX from 'xlsx';
import { MatSort } from '@angular/material/sort';
import { FormControl, FormGroup } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})

// class pour les requettes GET et POST.
export class ApiStat {

  baseurl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) {

  }
  sendFile(File1: any, File2: any, ecart: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append('ecart', ecart);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/mesure-csc/', formData, { headers: header })
  }
  sendFilePlus(File1: any, File2: any, ecartSup: any, ecartInf: any): Observable<any> {

    let formData = new FormData();
    formData.append('file1', File1, File.name);
    formData.append('file2', File2, File.name);
    formData.append('ecartSup', ecartSup);
    formData.append('ecartInf', ecartInf);
    console.log(formData)

    var header = new HttpHeaders();
    header.append('Content-Type', 'multipart/form-data');
    return this.http.post(this.baseurl + '/mesure-csc-plus/', formData, { headers: header })
  }
}

// interface StatData qui précise les données affichées dans le tableau ainsi que leur type.
export interface StatData {
  ID: string;
  NAVIRE: string;
  SENS: string;
  DATE: string;
  ECART: string;
  NIVEAU: string;
  VENTE: string;
  VENTEJ: string;

}
@Component({
  selector: 'app-mesure-csc',
  templateUrl: './mesure-csc.component.html',
  styleUrls: ['./mesure-csc.component.css'],
  providers: [ApiStat]
})
export class MesureCscComponent {

  options: any
  dataFrame: any;
  @ViewChild('TABLE') table: ElementRef;
  displayedColumns: string[] = ['ID', 'NAVIRE', 'SENS', 'DATE', 'ECART', 'VENTE', 'VENTEJ'];
  dataSource: MatTableDataSource<StatData>;

  ecartSup: string = null;
  ecartInf: string = null;
  annee: string;
  FecartSup = new FormControl('');
  FecartInf = new FormControl('');
  df1: any = null;
  df2: any = null;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;
  value: number=10;

  constructor(private DATACLEANING: ApiStat, public dialog: MatDialog) {
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

  changed1(value) {
    this.ecartSup = value.target.value
  }
  changed2(value) {
    this.ecartInf = value.target.value
  }
  deleteData() {
    this.dataSource = new MatTableDataSource([]);
  }

  dashboard() {
    this.getOptions()

    const dialogRef = this.dialog.open(DialogOverviewExampleDialog, {
      width: '800px',
      data: this.options
    });
    Highcharts.chart('container', this.options)
  }
  printTable() {
    const printContents = document.getElementById("reporting").outerHTML
    var newWin = window.open("");
    newWin.document.write(`
      <html>
        <head>
          <title>Mesure Vente CSC</title>
          <style>
          table th, table td {
            border-top: 0.5px solid #000;
            padding:0.5em;
          }
          </style>
        </head>
    <body onload="window.print();window.close()">${printContents}</body>
      </html>`
    );
    newWin.print();
    newWin.close();

  }
  // function executed when user click on Reporting button
  createFile = () => {
    if (this.df1 != null && this.df2 != null) {
      if (this.ecartSup != null) {
        if (this.ecartInf == null) {
          this.value=0
          this.DATACLEANING.sendFile(this.df1, this.df2, this.ecartSup).subscribe(
            data => {
              this.value=10
              console.log(data)
              this.dataFrame = data;
              // to choose witch data gonna be showing in the table
              this.InitializeVisualization();
              // puts data into the datasource table
              this.dataSource = new MatTableDataSource(data);
              this.dataSource.sort = this.sort;
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
        if (this.ecartInf != null) {
          this.value=0
          this.DATACLEANING.sendFilePlus(this.df1, this.df2, this.ecartSup, this.ecartInf).subscribe(
            data => {
              this.value=10
              console.log(data)
              this.dataFrame = data;
              // to choose witch data gonna be showing in the table
              this.InitializeVisualization();
              // puts data into the datasource table
              this.dataSource = new MatTableDataSource(data);
              this.dataSource.sort = this.sort;
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
      }
    }
  }

  //observable for the checkBox execute every time the checkBox is changed
  executeVisualisation() {
    let c0: Observable<boolean> = this.ID.valueChanges;
    let c1: Observable<boolean> = this.NAVIRE.valueChanges;
    let c2: Observable<boolean> = this.SENS.valueChanges;
    let c3: Observable<boolean> = this.DATE.valueChanges;
    let c4: Observable<boolean> = this.ECART.valueChanges;
    let c5: Observable<boolean> = this.VENTE.valueChanges;
    let c6: Observable<boolean> = this.VENTEJ.valueChanges;

    merge(c0, c1, c2, c3, c4, c5, c6).subscribe(v => {
      this.columnDefinitions[0].show = this.ID.value;
      this.columnDefinitions[1].show = this.NAVIRE.value;
      this.columnDefinitions[2].show = this.SENS.value;
      this.columnDefinitions[3].show = this.DATE.value;
      this.columnDefinitions[4].show = this.ECART.value;
      this.columnDefinitions[5].show = this.VENTE.value;
      this.columnDefinitions[6].show = this.VENTEJ.value;

    });
  }
  exportTable() {
    const ws: XLSX.WorkSheet = XLSX.utils.table_to_sheet(this.table.nativeElement);
    const wb: XLSX.WorkBook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'CSC');


    let day = new Date().getDate()
    let mois = new Date().getMonth() + 1
    let annee = new Date().getFullYear()
    let date = "MesureCSC_" + day + "-" + mois + "-" + annee + ".xlsx"
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
      { def: 'ECART', label: 'ECART', show: this.ECART.value },
      { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
      { def: 'VENTEJ', label: 'VENTEJ', show: this.VENTEJ.value },

    ]
  }

  // declaring a form group for the checkBoxes
  form: FormGroup = new FormGroup({
    ID: new FormControl(true),
    NAVIRE: new FormControl(true),
    SENS: new FormControl(true),
    DATE: new FormControl(true),
    ECART: new FormControl(true),
    VENTE: new FormControl(true),
    VENTEJ: new FormControl(true),

  });

  // geting the checkBox
  ID = this.form.get('ID');
  NAVIRE = this.form.get('NAVIRE');
  SENS = this.form.get('SENS');
  DATE = this.form.get('DATE');
  ECART = this.form.get('ECART');
  VENTE = this.form.get('VENTE');
  VENTEJ = this.form.get('VENTEJ');


  //Control column ordering and which columns are displayed.
  columnDefinitions = [
    { def: 'ID', label: 'ID', show: this.ID.value },
    { def: 'NAVIRE', label: 'NAVIRE', show: this.NAVIRE.value },
    { def: 'SENS', label: 'SENS', show: this.SENS.value },
    { def: 'DATE', label: 'DATE', show: this.DATE.value },
    { def: 'ECART', label: 'ECART', show: this.ECART.value },
    { def: 'VENTE', label: 'VENTE', show: this.VENTE.value },
    { def: 'VENTEJ', label: 'VENTEJ', show: this.VENTEJ.value },
  ]

  // Filter data in witch columns is checked
  getDisplayedColumns(): string[] {
    return this.columnDefinitions.filter(cd => cd.show).map(cd => cd.def);
  }
  getOptions() {
    this.options = {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Report Quotidien CSC'
      },
      subtitle: {
        text: 'Somme des écarts'
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
        min: -250,
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

@Component({
  selector: 'dialog-overview-example-dialog',
  templateUrl: 'dialog.html',
})
export class DialogOverviewExampleDialog {

  constructor(
    public dialogRef: MatDialogRef<DialogOverviewExampleDialog>,
    @Inject(MAT_DIALOG_DATA) public data: StatData) { }

  onNoClick(): void {
    this.dialogRef.close();
  }
}
