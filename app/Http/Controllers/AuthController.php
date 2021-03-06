<?php
namespace App\Http\Controllers;

use App\User;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Hash;

class AuthController extends Controller
{
    public function login(Request $request): Response
    {
	    $data = $request->validate([
	        'email' => 'required|email',
	        'password' => 'required'
	    ]);

	    $user = User::where('email', $request->email)->first();

	    if (!$user || !Hash::check($request->password, $user->password)) {
	        return response([
	            'message' => ['These credentials do not match our records.']
	        ], 404);
	    }

	    $token = $user->createToken('my-app-token')->plainTextToken;

	    $response = [
	        'user' => $user,
	        'token' => $token
	    ];

	    return response($response, 201);
    }
}
