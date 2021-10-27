import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatItaCtnComponent } from './stat-ita-ctn.component';

describe('StatItaCtnComponent', () => {
  let component: StatItaCtnComponent;
  let fixture: ComponentFixture<StatItaCtnComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatItaCtnComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatItaCtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
