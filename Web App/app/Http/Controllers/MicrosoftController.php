<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class MicrosoftController extends Controller
{
    public function index(){
        $company = DB::table('company_info')->where('name', 'Microsoft')->first();

        $negative = DB::table('microsoft_data')->where('sentiment', 'negative')->get();
        $positive = DB::table('microsoft_data')->where('sentiment', 'positive')->get();
        $n_count = count($negative);
        $p_count = count($positive);

        $textblob_negative = DB::table('microsoft_textblob')->where('sentiment', 'negative')->get();
        $textblob_positive = DB::table('microsoft_textblob')->where('sentiment', 'positive')->get();
        $n_t_count = count($textblob_negative);
        $p_t_count = count($textblob_positive);
        return view('/companies/microsoft', [
            'negative' => $n_count, 
            'positive' => $p_count , 
            'company' => $company,
            't_negative' => $n_t_count,
            't_positive' => $p_t_count
            ]);

    }
}
