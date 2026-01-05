Als laatste was ik bij ueser_lessons aan het kijken. om de gemaakte lessons te geteren en laten zien. 
11:45 PM
12/25/2025

# -----

er is  een probleem : na dat ik het db verwijdert heb ik de server gestart de account is nog ingelogd! en de profile data bijven omdat ze zijn opgeslagen in de `request`. en User data zijn verwijdert want dit houen ik het niet in de `request`.


# -----

ik heb de `LessonForm` veranderd naar `Lesson` in de view `user_lessons` omdat ik de lessen van de user wil laten zien die hij heeft gemaakt. en niet de lessen waar hij is ingeschreven.

ik moet nog `lesson.thumbnail.url` size validatie toevoegen om er zeker van te zijn dat de afbeelding niet te groot is of te klein.


# ----

```
write it in: 1/4/2026 9:33 PM
LAST RQ: [04/Jan/2026 21:31:10] "GET /dash/new_lesson/ HTTP/1.1" 200 11461
```

ik wil de url van lessons en courses veranderen naar slug in plaats van id. zodat de url er beter uitziet. en om naar lesson te openen via course-slug/lesson-slug.
so :
/lessons/<int:id>  --> /lessons/<slug:course_slug>/<slug:lesson_slug>
/courses/<int:id>  --> /courses/<slug:course_slug>
this mean the slug field moet uniek zijn in de models Lesson en Course.