import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { TaskCardComponent } from './components/task-card/task-card.component';
import { HttpClientModule } from '@angular/common/http';
import { ResultTableComponent } from './components/result-table/result-table.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskCardComponent,
    ResultTableComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
