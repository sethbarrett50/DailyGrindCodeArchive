// To modify your controller to use the Thymeleaf template, you can modify the NoteController class from the previous post to return the template name and model attributes:

package com.example.notes;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/notes")
public class NoteController {
    
    @Autowired
    private NoteRepository noteRepository;

    @GetMapping("")
    public String getNotes(Model model) {
        model.addAttribute("notes", noteRepository.findAll());
        model.addAttribute("note", new Note());
        return "notes";
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<Note> getNoteById(@PathVariable("id") Long id) {
        Note note = noteRepository.findById(id).orElse(null);
        if (note == null) {
            return ResponseEntity.notFound().build();
        } else {
            return ResponseEntity.ok(note);
        }
    }
    
    @PostMapping("")
    public ResponseEntity<Note> createNote(@RequestBody Note note) {
    Note savedNote = noteRepository.save(note);
    return ResponseEntity.status(HttpStatus.CREATED).body(savedNote);
    }
    @PutMapping("/{id}")
    public ResponseEntity<Note> updateNote(@PathVariable("id") Long id, @RequestBody Note note) {
        Note existingNote = noteRepository.findById(id).orElse(null);
        if (existingNote == null) {
            return ResponseEntity.notFound().build();
        } else {
            existingNote.setTitle(note.getTitle());
            existingNote.setContent(note.getContent());
            Note updatedNote = noteRepository.save(existingNote);
            return ResponseEntity.ok(updatedNote);
        }
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteNoteById(@PathVariable("id") Long id) {
        noteRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}

// To test your Thymeleaf template, you can modify the NoteController class from the previous post to use the Thymeleaf template:

package com.example.notes;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/notes")
public class NoteController {
    
    @Autowired
    private NoteRepository noteRepository;

    @GetMapping("")
    public String getNotes(Model model) {
        model.addAttribute("notes", noteRepository.findAll());
        model.addAttribute("note", new Note());
        return "notes";
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<Note> getNoteById(@PathVariable("id") Long id) {
        Note note = noteRepository.findById(id).orElse(null);
        if (note == null) {
            return ResponseEntity.notFound().build();
        } else {
            return ResponseEntity.ok(note);
        }
    }
    
    @PostMapping("")
    public ResponseEntity<Note> createNote(@ModelAttribute Note note) {
        Note savedNote = noteRepository.save(note);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedNote);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<Note> updateNote(@PathVariable("id") Long id, @ModelAttribute Note note) {
        Note existingNote = noteRepository.findById(id).orElse(null);
        if (existingNote == null) {
            return ResponseEntity.notFound().build();
        } else {
            existingNote.setTitle(note.getTitle());
            existingNote.setContent(note.getContent());
            Note updatedNote = noteRepository.save(existingNote);
            return ResponseEntity.ok(updatedNote);
        }
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteNoteById(@PathVariable("id") Long id) {
        noteRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}