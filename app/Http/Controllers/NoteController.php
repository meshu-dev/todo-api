<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Database\Eloquent\Collection;
use App\Models\Note;

class NoteController extends Controller
{
    private Note $model;

    public function __construct(Note $model)
    {
        $this->model = $model;
    }

    public function index(): Collection
    {
        return $this->model->take(10)->get();
    }

    public function store(Request $request): Note
    {
        $request->validate($this->getValidationRules());

        return $this->model->create([
            'title' => $request->title,
            'text' => $request->text
        ]);
    }

    public function show(int $id): Note
    {
        return $this->model->findOrFail($id);
    }

    public function update(Request $request, int $id): void
    {
        $request->validate($this->getValidationRules());

        $this->model->where('id', $id)
          ->update([
            'title' => $request->title,
            'text' => $request->text
          ]);
    }

    public function destroy(int $id): void
    {
        $this->model->destroy($id);
    }

    public function getValidationRules(): array
    {
        return [
            'title' => 'required|min:3|max:255',
            'text' => 'required|min:3|max:500'
        ];
    }
}
