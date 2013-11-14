guard :shell do
  watch(/(.+)\.py/) do |m|
    title = 'Test'
    msg = `python #{m[1]}.py`
    status = ($?.success? && :success) || :failed

    n msg, title, status
    "-> #{msg}"
  end
end
