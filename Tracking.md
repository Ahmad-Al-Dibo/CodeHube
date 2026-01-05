# Tracking for every new functionality & feature

To keep track of every new functionality and feature added to the CursesPlatform project, we follow a structured approach:
1. **Feature Request Submission**: Any new functionality or feature request should be submitted through the project's issue tracker. Each request must include a detailed description, use cases, and any relevant references.
2. **Prioritization and Planning**: The development team will review the submitted requests, prioritize them based on factors such as user demand, project goals, and resource availability, and plan their implementation in upcoming sprints or releases.
3. **Implementation**: Once a feature is prioritized, it will be assigned to a developer or team for implementation. The development process will include coding, testing, and documentation.
4. **Testing and Quality Assurance**: After implementation, the new feature will undergo rigorous testing to ensure it meets the specified requirements and does not introduce any bugs or issues into the existing system.
5. **Deployment**: Upon successful testing, the new feature will be deployed to the production environment. Users will be notified of the new functionality through release notes or announcements.
6. **Feedback and Iteration**: After deployment, user feedback will be collected to assess the effectiveness of the new feature. Based on this feedback, further improvements or adjustments may be made in subsequent updates.

# -----

DATE: 12/25/2025 11:45 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: high
category: Bug & Improvement
status: Open

Title: Issue with User Session Persistence after Database Deletion
slug: user-session-persistence-issue


short-description: User sessions persist even after database deletion.

long-description: After deleting the database, the server was restarted and the user remained logged in. Profile data persisted because it was stored in the `request`, while user data were deleted since they weren't stored in the `request`.

steps-to-reproduce:
1. Delete the database.
2. Restart the server.
3. Observe that the user remains logged in with profile data intact.
expected-behavior: User should be logged out and all profile data should be cleared after database deletion.
actual-behavior: User remains logged in and profile data persists after database deletion.
suggested-fix: Implement a mechanism to clear user sessions and profile data from the `request` upon database deletion.
# -----
DATE: 1/4/2026 9:33 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: medium
category: Improvement
status: Confirmed on 1/5/2026 6:57 PM
Title: Change Lesson and Course URLs to Use Slugs Instead of IDs
slug: change-lesson-course-urls-to-slugs
short-description: Update lesson and course URLs to use slugs for better readability.
long-description: The current URLs for lessons and courses use integer IDs, which are not user-friendly. The URLs should be changed to use slugs instead, allowing for a more descriptive and readable format. For example, the lesson URL should change from `/lessons/<int:id>` to `/lessons/<slug:course_slug>/<slug:lesson_slug>`, and the course URL should change from `/courses/<int:id>` to `/courses/<slug:course_slug>`. This requires ensuring that the slug fields in the Lesson and Course models are unique.
steps-to-reproduce:
1. Access a lesson or course using the current ID-based URL.
2. Update the URL format to use slugs.
3. Ensure that the slug fields in the Lesson and Course models are unique.
expected-behavior: URLs for lessons and courses should use slugs instead of IDs, improving readability and SEO.
actual-behavior: URLs currently use integer IDs, which are less user-friendly.
suggested-fix: Modify the URL routing to accept slugs and ensure uniqueness of slug fields in the Lesson and Course models.
# -----
DATE: 12/30/2025 3:15 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: low
category: Improvement
status: Open
Title: Update LessonForm to Display User-Created Lessons
slug: update-lessonform-to-display-user-lessons
short-description: Modify the LessonForm view to show lessons created by the user.
long-description: The `LessonForm` in the `user_lessons` view currently displays lessons the user is enrolled in. It should be updated to show only the lessons that the user has created. Additionally, size validation for `lesson.thumbnail.url` needs to be added to ensure that uploaded images meet size requirements.
steps-to-reproduce:
1. Access the `user_lessons` view.
2. Observe that it shows lessons the user is enrolled in.
3. Update the view to display only lessons created by the user.
expected-behavior: The `user_lessons` view should display only the lessons created by the logged-in user.
actual-behavior: The `user_lessons` view currently shows lessons the user is enrolled in.
suggested-fix: Change the `LessonForm` to filter lessons by the logged-in user and add size validation for `lesson.thumbnail.url`.
# -----
DATE: 12/28/2025 10:00 AM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: medium
category: Improvement
status: Open
Title: Add Size Validation for Lesson Thumbnail URLs
slug: add-size-validation-for-lesson-thumbnails
short-description: Implement size validation for lesson thumbnail URLs.
long-description: To ensure that lesson thumbnails are of appropriate size, size validation needs to be added
for `lesson.thumbnail.url`. This will prevent users from uploading images that are too large or too small, maintaining a consistent appearance across the platform.
steps-to-reproduce:
1. Upload a lesson thumbnail that is too large.
2. Upload a lesson thumbnail that is too small.
3. Observe the behavior of the system.
expected-behavior: The system should reject thumbnails that are too large or too small.
actual-behavior: No size validation is currently in place for lesson thumbnails.
suggested-fix: Implement size validation for `lesson.thumbnail.url` to ensure uploaded images meet size requirements.
# -----
DATE: 12/27/2025 2:30 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: low
category: Bug
status: Open
Title: Lesson Thumbnail URL Not Validated for Size
slug: lesson-thumbnail-url-size-validation
short-description: Lesson thumbnail URLs lack size validation.
long-description: The current implementation does not validate the size of lesson thumbnail URLs. This can lead to issues with image display if the thumbnails are too large or too small. Size validation should be added to ensure that all lesson thumbnails conform to specified dimensions.
steps-to-reproduce:
1. Upload a lesson thumbnail without size restrictions.
2. Observe the display of the thumbnail in the lesson view.
expected-behavior: Lesson thumbnails should be validated for size to ensure proper display.
actual-behavior: There is no size validation for lesson thumbnail URLs.
suggested-fix: Add size validation for lesson thumbnail URLs to ensure they meet the required dimensions.
# -----
DATE: 12/26/2025 4:20 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: medium
category: Improvement
status: Open
Title: Refactor User Lessons View to Show Created Lessons
slug: refactor-user-lessons-view
short-description: Change the user lessons view to display lessons created by the user.
long-description: The current user lessons view uses `LessonForm` to display lessons the user is enrolled in. This should be refactored to show only the lessons that the user has created. This change will provide a more relevant experience for users looking to manage their own content.
steps-to-reproduce:
1. Access the user lessons view.
2. Observe that it shows lessons the user is enrolled in.
3. Refactor the view to display only lessons created by the user.
expected-behavior: The user lessons view should display only the lessons created by the logged-in user.
actual-behavior: The user lessons view currently shows lessons the user is enrolled in.
suggested-fix: Update the user lessons view to filter lessons by the logged-in user.
# -----
DATE: 1/5/2026 6:20 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: high
category: Improvement
status: Open
Title: Lesson Creation Fails to Submit Without Thumbnail Image Change
slug: lesson-creation-redirect-issue
short-description: Lesson creation form does not submit properly when thumbnail image is not modified.
long-description: When creating a new lesson, clicking the submit button without modifying the thumbnail image causes the form to redirect back to the same page without saving the lesson, even though all required fields are filled. The server responds with HTTP 200 and returns the form page. However, if the thumbnail image is changed, the lesson is created successfully. This indicates a validation or form handling issue specific to the thumbnail field.
steps-to-reproduce:
1. Fill out all fields in the lesson creation form (title, description, content, etc.).
2. Do NOT change the thumbnail image field.
3. Click the submit button.
4. Observe that the page refreshes without creating the lesson.
5. Verify that changing the thumbnail image allows the form to submit successfully.
expected-behavior: The lesson should be created successfully and the user should be redirected to the appropriate page after clicking the submit button, regardless of whether the thumbnail image is modified.
actual-behavior: The form submission fails silently and redirects back to the same page when the thumbnail image is not changed, even with all other fields properly filled.
suggested-fix: Review the lesson creation logic and form validation to ensure the thumbnail field does not enforce unexpected validation constraints when the value remains unchanged. Consider allowing optional thumbnail updates or implementing proper default handling for unchanged file fields.
# -----

DATE: 1/5/2026 7:10 PM
Development TEAM: Startup team
reported-by: Ahmad Al Dibo
importance: medium
category: Improvement
status: Open
Title: user icon or picture not showing in lesson view or authers.
slug: user-icon-not-showing-in-lesson-view
short-description: User icon or picture is not displayed in the lesson view or author sections.
long-description: In the lesson view and author sections, the user icon or picture is not being displayed as expected. This issue affects the visual representation of authors and may impact user experience. The implementation needs to be reviewed to ensure that the correct image URLs are being used and that the images are properly rendered in the templates.
steps-to-reproduce:
1. Navigate to a lesson view or author section.
2. Observe that the user icon or picture is not displayed.
expected-behavior: The user icon or picture should be displayed correctly in the lesson view and
author sections.
actual-behavior: The user icon or picture is not shown in the lesson view or author
sections.
suggested-fix: Review the template code and ensure that the correct image URLs are being used to display user icons or pictures. Verify that the images are accessible and properly rendered in the HTML.
# -----