import { ref, reactive } from 'vue'

export function useForm(initialFields, validationRules = {}) {
  const formRef = ref(null)
  const form = reactive({ ...initialFields })
  const rules = reactive({ ...validationRules })
  const submitting = ref(false)
  const error = ref(null)

  async function validate() {
    if (!formRef.value) return true
    return formRef.value.validate().catch(() => false)
  }

  async function handleSubmit(submitFn) {
    const valid = await validate()
    if (!valid) return false

    submitting.value = true
    error.value = null
    try {
      await submitFn(form)
      return true
    } catch (err) {
      error.value = err.response?.data?.detail || err.message
      return false
    } finally {
      submitting.value = false
    }
  }

  function resetForm() {
    Object.keys(initialFields).forEach((key) => {
      form[key] = initialFields[key]
    })
    formRef.value?.resetFields()
  }

  return { formRef, form, rules, submitting, error, handleSubmit, resetForm }
}
