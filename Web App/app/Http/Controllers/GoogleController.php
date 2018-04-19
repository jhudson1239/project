<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class GoogleController extends Controller
{
    public function index(){
        $company = DB::table('company_info')->where('name', 'Google')->first();

        $negative = DB::table('google_data')->where('sentiment', 'negative')->get();
        $positive = DB::table('google_data')->where('sentiment', 'positive')->get();
        $n_count = count($negative);
        $p_count = count($positive);

        $textblob_negative = DB::table('google_textblob')->where('sentiment', 'negative')->get();
        $textblob_positive = DB::table('google_textblob')->where('sentiment', 'positive')->get();
        $n_t_count = count($textblob_negative);
        $p_t_count = count($textblob_positive);
        return view('/companies/google', [
            'negative' => $n_count, 
            'positive' => $p_count , 
            'company' => $company,
            't_negative' => $n_t_count,
            't_positive' => $p_t_count
            ]);

    }
}
