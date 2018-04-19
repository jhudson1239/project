<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
Route::get('/', function(){
    return view('index');
});
Route::get('/google', 'GoogleController@index');
Route::get('/amazon', 'AmazonController@index');
Route::get('/microsoft', 'MicrosoftController@index');