guard :shell do
  watch('Gemfile') do |m|
    title = 'Bundler output'
    msg = 'Bundler Failure'
    status = :failed

    if `bundle`
      msg = 'Bundled'
      status = :status
    end

    n msg, title, status

      "-> #{msg}"
  end

  watch(/(.+)\.py/) do |m|
    title = 'Test output'
    msg = 'Python error'
    status = :failed

    output = `python #{m[1]}.py`

    if $?.success?
      msg = output
      status = :success
    end

    n msg, title, status

    "-> #{msg}"
  end
end
