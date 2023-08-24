$(document).ready(function() {
    // Smooth scrolling for navigation links
    $('.nav-list li a').click(function(e) {
        e.preventDefault();
        const targetSection = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(targetSection).offset().top
        }, 800);
    });
    
    // Load doctors based on selected department
    $('#department').change(function() {
        const selectedDepartment = $(this).val();
        const doctorSelect = $('#doctor');
        
        if (selectedDepartment) {
            doctorSelect.prop('disabled', true);
            
            $.ajax({
                url: `/get_doctors/${selectedDepartment}`,
                method: 'GET',
                success: function(data) {
                    doctorSelect.empty().append($('<option>', { value: '', text: 'Select a doctor' }));
                    
                    data.forEach(doctor => {
                        doctorSelect.append($('<option>', {
                            value: doctor.id,
                            text: doctor.name
                        }));
                    });
                    
                    doctorSelect.prop('disabled', false);
                },
                error: function(error) {
                    console.log('Error loading doctors:', error);
                }
            });
        } else {
            doctorSelect.empty().append($('<option>', { value: '', text: 'Select a department first' }));
            doctorSelect.prop('disabled', true);
        }
    });
    
    // Form handling using Ajax
    $('#appointmentForm').submit(function(e) {
        e.preventDefault();
        
        const formData = $(this).serialize();
        
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                $('#message').html('<div class="alert alert-success">' + response.message + '</div>');
            },
            error: function(error) {
                $('#message').html('<div class="alert alert-danger">An error occurred. Please try again later.</div>');
            }
        });
    });
    
    // Additional event listeners or JavaScript functionality here
});
