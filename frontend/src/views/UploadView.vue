
<template>
    <div style="display: flex; height: 90vh; align-items: center; justify-content: center;">
        <div class="card" style="padding: 30px;">
            <Toast />
            <FileUpload name="demo[]" url="/api/upload/" @upload="onAdvancedUpload($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
                <template #empty>
                    <p>Drag and drop files to here to upload.</p>
                </template>
            </FileUpload>
        </div>
    </div>
</template>

<script setup>
import { useToast } from "primevue/usetoast";
const toast = useToast();

const onAdvancedUpload = () => {
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
};
</script>
