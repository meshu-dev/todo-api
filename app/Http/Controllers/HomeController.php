<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Contracts\Support\Renderable;
use Illuminate\Http\JsonResponse;

class HomeController extends Controller
{
    /**
     * Show the application dashboard.
     */
    public function index(): Renderable
    {
        return view('home');
    }

    /**
     * Show the API status.
     */
    public function apiIndex(): JsonResponse
    {
        return response()->json([
            'status' => 'Ok'
        ]);
    }
}
