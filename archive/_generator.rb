MONTH_NAMES = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "Oktober", "November", "December"]

def write_template_file(path, permalink, title, options={})
    unless File.exists?(path)
        File.open(path, 'w') do |f|
            f.puts "---"
            f.puts "layout: archive"
            f.puts "permalink: '#{permalink}'"
            f.puts "redirect_from: 'archive/#{permalink}'"
            f.puts "title: '#{title}'"
            options.each do |k, v|
                f.puts "#{k}: '#{v}'"
            end
            f.puts "---"
        end
        puts "created archive page for #{title}"
    end
end


