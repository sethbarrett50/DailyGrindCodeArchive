// To create a Note entity, you can create a new Java class named "Note" in the "com.example.notes" package and add the following lines:

package com.example.notes;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Note {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    
    private String title;
    
    private String content;
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}

// To create a Note repository, you can create a new Java interface named "NoteRepository" in the "com.example.notes" package and add the following lines:
package com.example.notes;

import org.springframework.data.repository.CrudRepository;

public interface NoteRepository extends CrudRepository<Note, Long> {

}

// To test your Hibernate configuration, you can modify the NoteController class from the previous post to use the NoteRepository for storing and retrieving Note objects from the database:
package com.example.notes;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.httprequestMapping("/notes")
public class NoteController {
    @Autowired
    private NoteRepository noteRepository;
        
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
